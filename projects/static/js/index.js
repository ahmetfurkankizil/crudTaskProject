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
        },
        repositoryTypes: ['GitHub', 'GitLab', 'Bitbucket'],
        trackerTypes: ['GitHub', 'GitLab', 'Jira']
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
                    this.resetNewProject();
                })
                .catch(error => {
                    console.error('There was an error creating the project!', error);
                });
        },
        createRepository() {
            axios.post('http://127.0.0.1:8000/api/repositories/', this.newRepository)
                .then(response => {
                    this.resetNewRepository();
                })
                .catch(error => {
                    console.error('There was an error creating the repository!', error);
                });
        },
        createTracker() {
            axios.post('http://127.0.0.1:8000/api/trackers/', this.newTracker)
                .then(response => {
                    this.resetNewTracker();
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
        },
        editProject(project) {
            axios.put(`http://127.0.0.1:8000/api/projects/${project.id}/`, project)
                .then(response => {
                    this.fetchProjects();
                })
                .catch(error => {
                    console.error('There was an error updating the project!', error);
                });
        },
        resetNewProject() {
            this.newProject = {
                name: '',
                slug: '',
                description: '',
                language: '',
                repositories: [],
                trackers: []
            };
        },
        resetNewRepository() {
            this.newRepository = {
                title: '',
                url: '',
                type: '',
                email: '',
                token: '',
                project: ''
            };
        },
        resetNewTracker() {
            this.newTracker = {
                title: '',
                url: '',
                type: '',
                email: '',
                token: '',
                project: ''
            };
        }
    },
    mounted() {
        this.fetchProjects();
    }
});
