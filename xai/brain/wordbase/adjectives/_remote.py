

#calss header
class _REMOTE():
	def __init__(self,): 
		self.name = "REMOTE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
