new Vue({
    el: '#app',
    data: {
        message: 'Hello, Vue!',
        projects: [],
        newProject: {
            name: '',
            slug: '',
            description: '',
            language: '',
            repositories: [],
            trackers: []
        },
        newRepository: {
            title: '',
            url: '',
            type: '',
            email: '',
            token: '',
            project: ''
        },
        newTracker: {
            title: '',
            url: '',
            type: '',
            email: '',
            token: '',
            project: ''
        }
    },
    methods: {
        fetchProjects() {
            axios.get('http://127.0.0.1:8000/api/projects/')
                .then(response => {
                    this.projects = response.data;
                })
                .catch(error => {
                    console.error('There was an error fetching the projects!', error);
                });
        },
        createProject() {
            axios.post('http://127.0.0.1:8000/api/projects/', this.newProject)
                .then(response => {
                    this.projects.push(response.data);
                    this.newProject.name = '';
                    this.newProject.slug = '';
                    this.newProject.description = '';
                    this.newProject.language = '';
                })
                .catch(error => {
                    console.error('There was an error creating the project!', error);
                });
        },
        createRepository() {
            axios.post('http://127.0.0.1:8000/api/repositories/', this.newRepository)
                .then(response => {
                    this.newRepository.title = '';
                    this.newRepository.url = '';
                    this.newRepository.type = '';
                    this.newRepository.email = '';
                    this.newRepository.token = '';
                    this.newRepository.project = '';
                })
                .catch(error => {
                    console.error('There was an error creating the repository!', error);
                });
        },
        createTracker() {
            axios.post('http://127.0.0.1:8000/api/trackers/', this.newTracker)
                .then(response => {
                    this.newTracker.title = '';
                    this.newTracker.url = '';
                    this.newTracker.type = '';
                    this.newTracker.email = '';
                    this.newTracker.token = '';
                    this.newTracker.project = '';
                })
                .catch(error => {
                    console.error('There was an error creating the tracker!', error);
                });
        },
        deleteProject(projectId) {
            axios.delete(`http://127.0.0.1:8000/api/projects/${projectId}/`)
                .then(response => {
                    this.projects = this.projects.filter(project => project.id !== projectId);
                })
                .catch(error => {
                    console.error('There was an error deleting the project!', error);
                });
        }
    },
    mounted() {
        // Fetch projects on mount to ensure projects are displayed initially
        this.fetchProjects();
    }
});
