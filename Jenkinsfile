pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    credentialsId: '09bdb29f-0d21-45a7-beeb-cc4b17916025', // The ID you set earlier
                    url: 'https://github.com/22bcaf09/TurfManagement.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building project...'
                // Add build steps here
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                // Add test execution commands here
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Add deployment steps here
            }
        }
    }
}
