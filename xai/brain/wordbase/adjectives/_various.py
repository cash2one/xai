

#calss header
class _VARIOUS():
	def __init__(self,): 
		self.name = "VARIOUS"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
