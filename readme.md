Don't forget to be in the virtual environment

```
./env/Scripts/activate
```

Run Locally to Test

```
functions-framework --target increment_counter --debug
```

Package and Deploy

```
gcloud functions deploy increment_counter --runtime python39 --trigger-http --allow-unauthenticated
```
