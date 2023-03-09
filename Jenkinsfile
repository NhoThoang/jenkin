pipeline{
    agent any
    // stages{
    //     stage("Clone stage"){
    //         steps {
    //             git branch: "master", credentialsId: 'jenkins', url: "https://gitlab.com/thoang1/jenkins.git"
                
    //         }
    //     }

        stage('buid stage') {
            steps {
                withDockerRegistry(credentialsId: 'dockerhub', url: 'https://index.docker.io/v1/') {
                    sh 'docker build -t thobaby/node:v4 .'
                    sh 'docker push thobaby/node:v4'
 
               }                  
   
            }

        }
    }
}