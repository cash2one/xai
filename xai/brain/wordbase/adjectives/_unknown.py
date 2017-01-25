

#calss header
class _UNKNOWN():
	def __init__(self,): 
		self.name = "UNKNOWN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
