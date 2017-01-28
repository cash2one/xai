

#calss header
class _INSTANT():
	def __init__(self,): 
		self.name = "INSTANT"
		self.definitions = [u'happening immediately, without any delay: ', u'Instant food or drink is dried, usually in the form of a powder, and can be prepared very quickly by adding hot water: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
