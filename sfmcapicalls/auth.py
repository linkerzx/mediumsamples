def auth(clientId: str, 
         clientSecret: str
    ) -> requests.Response:
    
    end_point = "https://auth.exacttargetapis.com/v1" + "/requestToken" 
    headers = {'Content-type': 'application/json'}
    payload = {
        "clientId": clientId,
        "clientSecret": clientSecret,
        "accessType": "offline"
    }
    req = requests.post(
        end_point,
        headers=headers,
        data=json.dumps(payload)
    )
    return req
