

#calss header
class _USED():
	def __init__(self,): 
		self.name = "USED"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
