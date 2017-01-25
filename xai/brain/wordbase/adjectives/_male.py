

#calss header
class _MALE():
	def __init__(self,): 
		self.name = "MALE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
