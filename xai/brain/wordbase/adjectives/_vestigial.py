

#calss header
class _VESTIGIAL():
	def __init__(self,): 
		self.name = "VESTIGIAL"
		self.definitions = [u'being a small remaining part or amount', u'used to describe something, especially a part of the body, that has not developed completely, or has stopped being used and has almost disappeared: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
