

#calss header
class _PIERCING():
	def __init__(self,): 
		self.name = "PIERCING"
		self.definitions = [u'going through or into something: ', u'very cold, or making you feel very cold: ', u'(of a sound) high, loud, and unpleasant: ', u'a criticism, question, remark, etc. that is unpleasant or uncomfortable because it is expressed strongly, or it makes you think about or discuss something that you would prefer not to: ', u'used to describe the fact of a person looking very carefully at someone or something, especially when they are trying to discover something, often making people feel uncomfortable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
