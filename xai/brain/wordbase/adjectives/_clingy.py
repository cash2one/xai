

#calss header
class _CLINGY():
	def __init__(self,): 
		self.name = "CLINGY"
		self.definitions = [u'used to describe something that sticks onto someone or something tightly: ', u'A clingy person stays close to and depends on a person who is taking care of them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
