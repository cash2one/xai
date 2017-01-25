

#calss header
class _UP():
	def __init__(self,): 
		self.name = "UP"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
