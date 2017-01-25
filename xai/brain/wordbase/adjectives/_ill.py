

#calss header
class _ILL():
	def __init__(self,): 
		self.name = "ILL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
