pipeline{
    agent any
    stages{
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
        stage('SSH public'){
                steps{
                    
                    sshPublisher(publishers: [sshPublisherDesc(configName: 'remoteserver', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: 'docker-compose up -d', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', sourceFiles: 'docker-compose.yml')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
                    
                
                    
                }
        }
    }
}