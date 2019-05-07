#!groovy

/**
* Continuous Integration Jenkinsfile
*
* 
 * 
 * Setup:
* - Configure the environment variables accordingly
*/

// Declarative pipeline must be enclosed within a pipeline block
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
        DEVELOP_BRANCH = 'master' // Your Development Branch
        PROJECT_NAME = 'TestingCommit'
        COVERITY_HOST = '15.146.44.13'
        COVERITY_PORT = '8085'
        COVERITY_STREAM = 'fast-data'
        COVERITY_USER = 'user'
        COVERITY_PASS = 'x'
            
        EMAIL_TO = 'divith-reddy.gajjala@hpe.com'
        EMAIL_FROM = 'divith-reddy.gajjala@hpe.com'
        VIRTUAL_ENV = "${env.WORKSPACE}/venv"
    }

    /**
     * the stage directive should contain a steps section, an optional agent section, or other stage-specific directives
     * all of the real work done by a Pipeline will be wrapped in one or more stage directives
     */ 
   
    stages {
        
        stage ('Preparation') {
            steps {
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
            }
        }
                
        stage('Lint source') {
            steps {
                sh """
                  echo "hello world"
                  export PATH=${VIRTUAL_ENV}/bin:${PATH}
                  flake8 --exclude=venv* --statistics --ignore=E305, E112, E999
               """
            }  
        }           
               
        stage('Unit tests') {
            steps {
                sh """
                  export PATH=${VIRTUAL_ENV}/bin:${PATH}
                  pytest -vs --cov=calculator
               """
            }  
        }
            
        /*stage('Static Code Coverage') {
            steps {
               withCoverityEnv('Cov-Analysis') {
                   sh "cov-build --dir idir --fs-capture-search ${WORKSPACE}/src --no-command"
                   sh "cov-analyze --dir idir"
                   // sh "cov-commit-defects --dir idir --host ${COVERITY_HOST} --port ${COVERITY_PORT} --stream ${COVERITY_STREAM} --user ${COVERITY_USER} --password ${COVERITY_USER}"
               }
            }  
        } */          
    }
}    

