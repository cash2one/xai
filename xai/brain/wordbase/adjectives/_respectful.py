

#calss header
class _RESPECTFUL():
	def __init__(self,): 
		self.name = "RESPECTFUL"
		self.definitions = [u'showing admiration for someone or something: ', u'showing politeness or honour to someone or something: ', u'to accept that something is important and not to try to change it or cause offence: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
