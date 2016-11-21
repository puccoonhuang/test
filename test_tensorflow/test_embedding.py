import tensorflow as tf


with tf.Session() as sess:
    emb = tf.Variable(tf.truncated_normal([4, 10], 0.0, 1.0, dtype=tf.float32))
    x   = tf.constant([0, 2])
    res = tf.nn.embedding_lookup(emb, x)

    x2   = tf.constant([[0, 2],
                      [1, 2]])
    res2 = tf.nn.embedding_lookup(emb, x2)
    res2_expanded = tf.expand_dims(res2, -1)
    res3 = tf.transpose(res2, [1, 0, 2])
    res3 = tf.reshape(res3, [-1, 10])
    res3 = tf.split(0, 2, res3)

    tf.initialize_all_variables().run()

    print sess.run(emb)
    print

    print sess.run(res)
    print

    print sess.run(res2)
    print

    print sess.run(res2_expanded)
    print

    print sess.run(res3)
    print
