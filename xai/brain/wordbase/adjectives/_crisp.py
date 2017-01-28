

#calss header
class _CRISP():
	def __init__(self,): 
		self.name = "CRISP"
		self.definitions = [u'hard enough to be broken easily', u'used to describe cooked foods, such as pastry and biscuits, that are well cooked so that they are just dry and hard enough', u'Crisp fruit or vegetables are fresh and firm: ', u'Crisp paper or cloth is stiff and smooth: ', u'A crisp sound or image is very clear: ', u'A crisp way of speaking, writing, or behaving is quick, confident, and effective: ', u'Crisp weather is cold, dry, and bright: ', u'Crisp air is cold, dry, and fresh: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
