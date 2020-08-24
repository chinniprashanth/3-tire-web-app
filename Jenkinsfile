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
       #docker tag the images
       docker tag 3-tire-web-app_api:latest 643370628328.dkr.ecr.us-east-2.amazonaws.com/3-tire-web-app_api:latest
       docker tag 3-tire-web-app_webapp:latest 643370628328.dkr.ecr.us-east-2.amazonaws.com/3-tire-web-app_webapp:latest
       docker tag postgress:latest 643370628328.dkr.ecr.us-east-2.amazonaws.com/postgress:latest
       
       #docker publish to ecr repo
       docker push 643370628328.dkr.ecr.us-east-2.amazonaws.com/3-tire-web-app_api
       docker push 643370628328.dkr.ecr.us-east-2.amazonaws.com/3-tire-web-app_webapp
       docker push 643370628328.dkr.ecr.us-east-2.amazonaws.com/postgress
      '''
      
      }
     }
    stage ('Eks cluster creation using terraform'){
     steps {
     sh ''' 
        cd terraform/
        terraform init
        terraform plan
        terraform apply -auto-approve
        '''
     }
    }    
   stage ('Ansible deployment to EKS'){
     steps {
     sh '''  
     cd ../3-tire-web-app/
     ansible-playbook k8.yaml
     '''
   }

  }
 } 
}   
