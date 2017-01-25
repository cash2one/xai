

#calss header
class _MEDICAL():
	def __init__(self,): 
		self.name = "MEDICAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
