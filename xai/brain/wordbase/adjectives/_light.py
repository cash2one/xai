

#calss header
class _LIGHT():
	def __init__(self,): 
		self.name = "LIGHT"
		self.definitions = [u'not weighing a lot: ', u'Light clothes are made of thin material that allows you to be cool: ', u'lit by the natural light of the day: ', u'(of colours) pale: ', u'entertaining and easily understood, but not serious and not intended to make you think: ', u'to behave as if a situation, especially a problem, is not serious or important: ', u'not great in strength or amount: ', u'someone who eats/drinks/smokes only a little', u'someone who is easily woken up by noise, etc.', u'A light meal is small and easy to digest: ', u'used to describe alcoholic drinks that are not strong in flavour: ', u'needing only a very small amount of effort: ', u'A light sentence in prison is a short one: ', u'to do something quickly and easily: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
