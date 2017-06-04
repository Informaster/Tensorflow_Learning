import tensorflow as tf

#Computational Graph

node1 = tf.constant(3.0)
node2 = tf.constant(4.0)
print(node1, node2)

node3 = tf.add(node1, node2)
print(node3)

node1 = tf.summary.scalar("Hello", 1)

#Session (Runtime)
sess = tf.Session()
merge = tf.summary.merge_all()
writer = tf.summary.FileWriter("Logs\\first")
writer.add_graph(sess.graph)


print(sess.run([node1, node2, node3]))

