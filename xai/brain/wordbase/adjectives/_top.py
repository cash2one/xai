

#calss header
class _TOP():
	def __init__(self,): 
		self.name = "TOP"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
