

#calss header
class _HOME():
	def __init__(self,): 
		self.name = "HOME"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
