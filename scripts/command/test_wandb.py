import os, wandb
wandb.login(key=os.environ.get("WANDB_API_KEY", "2bd5495e28c7c16e92efa046f833ee9ed8048c05"))
api = wandb.Api()
a = api.artifact("cyfarwydd-new-york-university-org/wandb-registry-Motions/dance1_subject2:v0")
print("OK:", a.name, a.type)
