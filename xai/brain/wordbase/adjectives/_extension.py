

#calss header
class _EXTENSION():
	def __init__(self,): 
		self.name = "EXTENSION"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
