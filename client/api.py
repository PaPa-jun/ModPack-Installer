from PyQt6.QtCore import QThread, pyqtSignal
import requests

class CurseForgeClient(QThread):

    requestFinishSignal = pyqtSignal(object, str)

    def __init__(self, apiKey):
        super().__init__()
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'x-api-key': apiKey
        }
        self.func = None
        self.args = None
        self.kwargs = None

    def setTask(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def clearTask(self):
        self.func = None
        self.kwargs = None
    
    def searchMods(self, **params):
        """
        Search Mods.

        Return a list of mods.
        """
        params["gameId"] = 432
        params["classId"] = 4471
        response = requests.get('https://api.curseforge.com/v1/mods/search', headers=self.headers, params = params)
        return response.json()["data"]
    
    def getMod(self, modId: int):
        """
        Get a single mod.
        """
        response = requests.get(f"https://api.curseforge.com/v1/mods/{modId}", headers=self.headers)
        return response.json()["data"]

    def getMods(self, modIds: list):
        """
        Get a list of mods.
        """
        data = {
            "modIds": modIds,
            "filterPcOnly": True
        }
        response = requests.post("https://api.curseforge.com/v1/mods", json=data, headers=self.headers)
        return response.json()["data"]
    
    def getFeaturedMods(self):
        """
        Get a list of featured, popular and recently updated mods.
        """
        response = requests.post('https://api.curseforge.com/v1/mods/featured', headers = self.headers)
        return response.json()["data"]
    
    def getModDescription(self, modId):
        """
        Get the full description of a mod in HTML format.
        """
        response = requests.get(f'https://api.curseforge.com/v1/mods/{modId}/description', headers = self.headers)
        return response.json()["data"]
    
    def getModFile(self, modId, fileId):
        """
        Get a single file of the specified mod.
        """
        response = requests.get(f'https://api.curseforge.com/v1/mods/{modId}/files/{fileId}', headers = self.headers)
        return response.json()["data"]
    
    def getModFiles(self, modId, **params):
        """
        Get all files of the specified mod.
        """
        response = requests.get(f'https://api.curseforge.com/v1/mods/{modId}/files', headers = self.headers, params=params)
        return response.json()["data"]

    def getFiles(self, fileIds):
        """
        Get a list of files."
        """
        param = {
            "fileIds": fileIds
        }
        response = requests.post('https://api.curseforge.com/v1/mods/files', headers = self.headers, json=param)
        return response.json()["data"]
    
    def getModFileChangeLog(self, modId, fileId):
        """
        Get the changelog of a file in HTML format.
        """
        response = requests.get(f'https://api.curseforge.com/v1/mods/{modId}/files/{fileId}/changelog', headers = self.headers)
        return response.json()["data"]
    
    def getModFileDownloadUrl(self, modId, fileId):
        """
        Get a download url for a specific file.
        """
        response = requests.get(f'https://api.curseforge.com/v1/mods/{modId}/files/{fileId}/download-url', headers = self.headers)
        return response.json()["data"]

    def getMinecraftVersions(self):
        """
        Get all Minecraft versions.
        """
        response = requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json", headers=self.headers)
        data = response.json()
        
        versions = {
            'release': [],
            'snapshot': [],
            'old_beta': [],
            'old_alpha': []
        }
        
        for version in data['versions']:
            if version['type'] == 'release':
                versions['release'].append(version['id'])
            elif version['type'] == 'snapshot':
                versions['snapshot'].append(version['id'])
            elif version['type'] == 'old_beta':
                versions['old_beta'].append(version['id'])
            elif version['type'] == 'old_alpha':
                versions['old_alpha'].append(version['id'])
        
        return versions
    
    def run(self):
        if self.func is None:
            self.requestFinishSignal.emit(None, "No task specified")
            return
        
        try:
            result = self.func(*self.args, **self.kwargs)
            self.requestFinishSignal.emit(result, "")
            self.clearTask()
        except Exception as e:
            self.requestFinishSignal.emit(None, str(e))

client = CurseForgeClient("$2a$10$7MBRs6xZiY1ijvGNoGgwkOPqOunnyX/ssqu16WiSmrnWzM/9uoFOi")