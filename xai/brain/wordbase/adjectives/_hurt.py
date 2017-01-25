

#calss header
class _HURT():
	def __init__(self,): 
		self.name = "HURT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
