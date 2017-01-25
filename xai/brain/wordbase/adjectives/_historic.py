

#calss header
class _HISTORIC():
	def __init__(self,): 
		self.name = "HISTORIC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
