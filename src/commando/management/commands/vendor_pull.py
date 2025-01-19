from django.core.management.base import BaseCommand
# from src.helper.downloder import extractor
from pathlib import Path
from django.conf import settings
from helper import extractor
class Command(BaseCommand): 

    vendor_path = {

        "flowbite_css.css" : "https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.css",
        "flowbite_js.js" : "https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.js",
    }



    STATICFILES_URL = getattr(settings, "VENDORS_URL",None)

    def handle(self,*args,**kwargs) : 
        complited = []
        if not self.STATICFILES_URL:
            self.STATICFILES_URL.mkdir(parents=True, exist_ok=True)
            self.stdout.write(self.style.ERROR("VENDORS_URL not set in settings."))
            raise ValueError("STATICFILES_URL is not defined in settings.py")
        
        for name, url in self.vendor_path.items():        
            outpath = self.STATICFILES_URL/name
            try:
                result = extractor(url, outpath)
                if result:
                    complited.append(name)
                    self.stdout.write(self.style.SUCCESS(f"Successfully downloaded {name}")) 
            
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed to download {name}"))
                raise ValueError(f"Error in downloading file: {e}")
            
        if set(complited) == self.vendor_path.keys():
                self.stdout.write(self.style.SUCCESS("All files downloaded successfully"))

        else: 
                self.stdout.write(self.style.ERROR("Some files failed to download"))