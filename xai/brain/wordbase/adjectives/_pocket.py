

#calss header
class _POCKET():
	def __init__(self,): 
		self.name = "POCKET"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
