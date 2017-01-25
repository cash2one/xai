

#calss header
class _MINOR():
	def __init__(self,): 
		self.name = "MINOR"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
