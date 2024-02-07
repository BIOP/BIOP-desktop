# Run BIOP-desktop on Kubernetes

## Kubernetes vanilla

### Create pod 

#### ... using deployment

```bash
kubectl apply -f biop-desktop-deployment.yaml
```
#### ... using job
```bash
kubectl apply -f biop-desktop-job.yaml
```

## Access to jupyter
```bash
kubectl port-forward $(kubectl get pods -l app=biop-desktop -o name|head -n 1) 8888
```

```bash
kubectl port-forward biop-desktop-0-0 8888
```
Open [http://127.0.0.1:8888](http://127.0.0.1:8888) in your web browser

## Cleanup
```bash
kubectl delete deployments.apps,jobs.batch -l app=biop-desktop
```


## Kubernetes RunAI

### Create pod using job
```bash
kubectl apply -f biop-desktop-runaijob.yaml
```

### Access to jupyter
```bash
kubectl port-forward $(kubectl get pods -l app=biop-desktop -o name|head -n 1) 8888
```
or
```bash
kubectl port-forward biop-desktop-0-0 8888
```
Open [http://127.0.0.1:8888](http://127.0.0.1:8888) in your web browser

### Cleanup
```bash
kubectl delete runaijobs.run.ai -l app=biop-desktop
```


# Pull image on nodes
kubectl create -f image-puller.yaml 