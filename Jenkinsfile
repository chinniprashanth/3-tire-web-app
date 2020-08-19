pipeline {
   agent any
    
   tools {
      // Install the Maven version configured as "M3" and add it to the path.
      jdk 'JAVA'
      maven "Maven"
   }
   
   
   stages {
   stage('checkout') {
         steps {
            // Get some code from a GitHub repositoryn
            git 'https://github.com/chinniprashanth/3-tire-web-app.git'
        }
       
        }
    
	stage ('Build Docker Image'){
     steps {
     sh '''
      cd 3-tire-web-app/
	    docker-compose up --build 
     '''

   }
  }
   stage ('Publish Docker Image'){
     steps {
     sh '''
	     aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 643370628328.dkr.ecr.us-east-2.amazonaws.com
       docker push 643370628328.dkr.ecr.us-east-2.amazonaws.com/docker-frontend-backend-db_api
       docker push 643370628328.dkr.ecr.us-east-2.amazonaws.com/docker-frontend-backend-db_webapp
       docker push 643370628328.dkr.ecr.us-east-2.amazonaws.com/postgres
      '''
      
      }
     }
   }

  }
