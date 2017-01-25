

#calss header
class _RUNNING():
	def __init__(self,): 
		self.name = "RUNNING"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
