# Bad App No Biscuit

## A very bad app that is slow, to show off monitoring and scaling systems

## Steps

You can [deploy this application to IBM Cloud](https://cloud.ibm.com/developer/appservice/starter-kits/python-flask-app) or [build it locally](#building-locally) by cloning this repo first. Once your app is live, you can access the `/health` endpoint to build out your cloud native application. See the [upstream example repo](https://github.com/IBM/python-flask-app).

### Deploying to IBM Cloud

```
cd deployment
kubectl apply -f banb-deployment.yaml
```

### Load testing

```
ab -n 1000 -c 30 ${URL}/fib/100000
```

### Set up autoscaling

```
cd deployment
kubectl apply -f autoscaling-config.yaml
```

## Next Steps
* Learn more about the services and capabilities of [IBM Cloud](https://cloud.ibm.com).
* Explore other [sample applications](https://cloud.ibm.com/developer/appservice/starter-kits) on IBM Cloud.

## License

This sample application is licensed under the Apache License, Version 2. Separate third-party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache License FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)

