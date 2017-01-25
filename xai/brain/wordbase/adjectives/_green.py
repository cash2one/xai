

#calss header
class _GREEN():
	def __init__(self,): 
		self.name = "GREEN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
