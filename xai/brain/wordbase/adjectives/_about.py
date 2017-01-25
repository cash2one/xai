

#calss header
class _ABOUT():
	def __init__(self,): 
		self.name = "ABOUT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
