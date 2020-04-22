Get company name of given Mac address


Environment: 
          Python 2 or 3
          
          
Libraries to be used for creating a API:
          Flask
          pip install flask


User input: 
          Macaddress
          Format: 
                88:53:2E:    (or)
                88-53-2E
                
                
To run in a command prompt:


      curl -i -H "Content-Type: application/json" -X POST -d '{"macaddress":"88:53:2E:67:07:BE"}' http://localhost:5000/macaddress
 
      
Responses:


      200 - Sucess 
      400 - Bad request ( user doesn't give macaddress in proper format)
      
