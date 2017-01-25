

#calss header
class _VEGETABLE():
	def __init__(self,): 
		self.name = "VEGETABLE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
