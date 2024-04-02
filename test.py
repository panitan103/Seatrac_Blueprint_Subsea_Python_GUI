try:
    import lightrun
    lightrun.enable(company_key='aad7d1c9-2288-4036-b4f0-d4b9c35f4c9f')
except ImportError as e:
    print("Error importing Lightrun: ", e)