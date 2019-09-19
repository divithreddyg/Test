#!groovy

pipeline {

    // agent section specifies where the entire Pipeline will execute in the Jenkins environment
    agent any

    options {
        buildDiscarder(
            // Only keep the 10 most recent builds
            logRotator(numToKeepStr:'5'))
    }    

    environment {
        REPO_URL = 'git@github.com:divithreddyg/TestingCommit.git' // Your GitHub Repository
        DEVELOP_BRANCH = 'Testing2' // Your Development Branch
        PROJECT_NAME = 'Test'
        VIRTUAL_ENV = "${env.WORKSPACE}/venv"
    }
   
    stages {
        
        stage ('Preparation') {
            
            steps {
                script {
                    try{
                        sh """
                            echo ${SHELL}
                            [ -d venv ] && rm -rf venv
                            python3.6 -m venv venv
                            export http_proxy=http://web-proxy.in.hpecorp.net:8080
                            export https_proxy=http://web-proxy.in.hpecorp.net:8080
                            export PATH=${VIRTUAL_ENV}/bin:${PATH}
                            pip install --upgrade pip
                           pip install -r requirements.txt
                        """
                        CURRENT_BUILD = 'SUCCESS';
                    } catch(Exception err) {
                        CURRENT_BUILD = 'FAILURE';
                    }
                
                }
            }
            post {
        always {
            //archiveArtifacts artifacts: '**/*.jar', fingerprint: true
            archiveArtifacts '**/*.xml'
        }
    }
        }
                
        stage('Lint source') {
                steps {
                    script{
                        try {
                            
                            sh """
                              echo "hello world"
                              export PATH=${VIRTUAL_ENV}/bin:${PATH}
                              flake8 --exclude=venv* --statistics --ignore=E305, E112, E999
                           """
                        } catch(Exception err) {
                            CURRENT_BUILD = 'FAILURE';
                        }
                    }
                }  
                post {
            always {
                //archiveArtifacts artifacts: '**/*.jar', fingerprint: true
                archiveArtifacts '**/*.xml'
            }
        }
    }           
               
        stage('Unit tests') {
                steps {
                    script {
                        try {
                            sh """
                              export PATH=${VIRTUAL_ENV}/bin:${PATH}
                              pytest -vs --cov=calculator  --junitxml=out_report.xml
                           """
                        }catch(Exception err) {
                            CURRENT_BUILD = 'FAILIURE'
                        }
                        
                    }
                }  
                post {
            always {
                //archiveArtifacts artifacts: '**/*.jar', fingerprint: true
                junit 'out_report.xml'
            }
        }
    }   
}
        
    post {
        success {
            script {
                python3 remove_issues.py
            }
        }
        failure {
            script {
                python3 add_issues.py
            }
        }
    } 
}
