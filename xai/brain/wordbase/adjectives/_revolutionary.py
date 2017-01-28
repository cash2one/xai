

#calss header
class _REVOLUTIONARY():
	def __init__(self,): 
		self.name = "REVOLUTIONARY"
		self.definitions = [u'involved in or relating to a revolution: ', u'completely new and having a great effect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
