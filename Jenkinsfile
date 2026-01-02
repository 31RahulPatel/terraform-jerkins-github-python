pipeline {
    agent any
    
    triggers {
        githubPush()
    }
    
    stages {
        stage('Deploy to Private Instance') {
            steps {
                sshagent(['ec2-ssh-key']) {
                    sh '''
                        # Copy files to private instance
                        scp -o StrictHostKeyChecking=no -r python-app ec2-user@10.0.2.101:/opt/
                        
                        # Deploy on private instance
                        ssh -o StrictHostKeyChecking=no ec2-user@10.0.2.101 "
                            cd /opt/python-app
                            sudo docker build -t python-app .
                            sudo docker stop python-app || true
                            sudo docker rm python-app || true
                            sudo docker run -d --name python-app -p 8000:8000 python-app
                            sudo docker ps
                        "
                    '''
                }
            }
        }
    }
}