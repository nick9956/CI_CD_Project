pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                script {
                    // Install Poetry
                    sh 'curl -sSL https://install.python-poetry.org | python3 -'
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Install project dependencies
                    sh 'poetry install'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Ensure the script is executable
                    sh 'chmod +x ./run_py_tests.sh'
                    // Run tests and generate reports
                    sh './run_py_tests.sh'
                }
            }
        }
    }
    post {
        always {
            // Clean up the workspace after the pipeline runs
            cleanWs()
        }
        success {
            // Actions to perform if the pipeline was successful
            echo 'Tests ran successfully!'
        }
        failure {
            // Actions to perform if the pipeline failed
            echo 'Tests failed. Check the logs for details.'
        }
    }
}