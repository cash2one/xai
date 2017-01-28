

#calss header
class _RETIRING():
	def __init__(self,): 
		self.name = "RETIRING"
		self.definitions = [u'unwilling to be noticed or to be with other people: ', u'used to refer to someone who is planning to leave their job and usually to stop working permanently because of age: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
