pipeline{
    agent any
    stages{
        stage("Clone stage"){
            steps{
                git credentialsId: 'webhook2', url: "https://gitlab.com/thoang1/jenkins.git"
            }
        }


        stage("clones stage"){
            step{
                withDockerRegistry(credentialsId: 'dockerhub', url: 'https://index.docker.io/v1/') {
                    sh 'docker build -t thobaby/node:v2 .'
                    sh 'docker push thobaby/node:v2'
                }
            }


        }
    }
}