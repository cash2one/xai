

#calss header
class _STANDING():
	def __init__(self,): 
		self.name = "STANDING"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
