

#calss header
class _OFFICIAL():
	def __init__(self,): 
		self.name = "OFFICIAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
