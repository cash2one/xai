

#calss header
class _PATIENT():
	def __init__(self,): 
		self.name = "PATIENT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
