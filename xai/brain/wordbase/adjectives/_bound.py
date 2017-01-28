

#calss header
class _BOUND():
	def __init__(self,): 
		self.name = "BOUND"
		self.definitions = [u'certain or extremely likely to happen: ', u'to be seriously intending to do something: ', u'I am certain: ', u'having a moral or legal duty to do something: ', u'tied with rope, cord, string, etc.: ', u'(of a book) having a cover made of paper, leather, or other material: ', u'going to: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
